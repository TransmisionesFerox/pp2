import psycopg2
import json  # For handling game state if you choose JSON

DB_HOST = "your_host"
DB_NAME = "your_database"
DB_USER = "your_user"
DB_PASSWORD = "your_password"

def connect():
    conn = None
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        print("Connected to PostgreSQL database.")
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
    return conn

def get_user_id(conn, username):
    cursor = conn.cursor()
    sql = "SELECT user_id FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def create_user(conn, username):
    cursor = conn.cursor()
    sql = "INSERT INTO users (username) VALUES (%s) RETURNING user_id"
    try:
        cursor.execute(sql, (username,))
        user_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        return user_id
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        cursor.close()
        return None
    except (Exception, psycopg2.Error) as error:
        print(f"Error creating user: {error}")
        conn.rollback()
        cursor.close()
        return None

def get_current_level(conn, user_id):
    cursor = conn.cursor()
    # Assuming the 'level' in user_scores represents the level played.
    # You might want to adjust this query based on how you define "current level"
    sql = "SELECT level FROM user_scores WHERE user_id = %s ORDER BY saved_at DESC LIMIT 1"
    cursor.execute(sql, (user_id,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else 1 # Default to level 1 if no score exists

def handle_user_login(conn):
    username = input("Enter your username: ")
    user_id = get_user_id(conn, username)

    if user_id:
        print(f"Welcome back, {username}!")
        current_level = get_current_level(conn, user_id)
        print(f"Your current level is: {current_level}")
        return user_id
    else:
        print(f"User '{username}' not found. Creating new user...")
        new_user_id = create_user(conn, username)
        if new_user_id:
            print(f"Welcome, {username}! Starting at level 1.")
            return new_user_id
        else:
            print("Error creating user. Please try again.")
            return None

# Example of how you might define levels in your game logic
levels_data = {
    1: {"name": "Beginner", "speed": 5, "walls": []},
    2: {"name": "Intermediate", "speed": 8, "walls": [(5, 5), (5, 6), (6, 6)]},
    3: {"name": "Advanced", "speed": 12, "walls": [(2, 3), (4, 7), (8, 1), (9, 9), (9, 8)]},
    # ... more levels
}

def get_level_details(level):
    return levels_data.get(level, {"name": "Unknown", "speed": 5, "walls": []})

if __name__ == '__main__':
    conn = connect()
    if conn:
        user_id = handle_user_login(conn)
        if user_id:
            # Start the snake game with the obtained user_id
            # You would then use this user_id to save scores and game states
            pass
        conn.close()

def save_game_state(conn, user_id, score, level, game_state):
    cursor = conn.cursor()
    sql = "INSERT INTO user_scores (user_id, score, level, game_state) VALUES (%s, %s, %s, %s)"
    try:
        # Serialize the game_state to a string (e.g., JSON)
        serialized_game_state = json.dumps(game_state)
        cursor.execute(sql, (user_id, score, level, serialized_game_state))
        conn.commit()
        print("Game state saved.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error saving game state: {error}")
        conn.rollback()
    finally:
        if cursor:
            cursor.close()

# Example of how you might use the save function within your game loop
if __name__ == '__main__':
    conn = connect()
    if conn:
        user_id = handle_user_login(conn)
        if user_id:
            # Simulate game variables
            current_score = 150
            current_level = 2
            current_game_data = {
                "snake_positions": [(10, 5), (10, 6), (10, 7)],
                "food_position": (3, 8),
                "direction": "up"
            }

            # Simulate pause and save
            save_game_state(conn, user_id, current_score, current_level, current_game_data)

        conn.close()

