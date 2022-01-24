


def create_table():
    dat = sqlite3.connect('heart.db')
    c = dat.cursor()
    c.execute("""
            CREATE TABLE sensor(
                [id] INTEGER PRIMARY KEY,
                [pulso] INTEGER NOT NULL
            );
            """)
    dat.commit()
    dat.close()