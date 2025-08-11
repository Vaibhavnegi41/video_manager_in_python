import sqlite3 as s

connection=s.connect('youtube_videos.db')
cursor=connection.cursor()

cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL ,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print('\n')
    print("*"*100)
    for row in cursor.fetchall():
        print(f"{row[0]}. {row[1]} , Duration:{row[2]}")

    print('\n')
    print("*"*100)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time)VALUES(?,?)",(name,time))
    connection.commit()
    
def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name=? time=? WHERE id=?",(name,time,video_id))
    connection.commit()
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    connection.commit()

def main():
    while True:
        print("\n Youtube Manager ! || choose any option")
        print("1.List all youtube videos ")
        print("2.Add a youtube video ")
        print("3.Update a youtube video details ")
        print("4. Delete a youtube videos ")
        print("5. exit the app ")

        choice=input("enter your choice :")

        if(choice=='1'):
            list_videos()

        elif(choice=='2'):
            name=input("enter the video name :")
            time=input("enter video time :")
            add_video(name,time)

        elif(choice=='3'):
            video_id=input("enter the video number to be updated :")
            name=input("enter the video name :")
            time=input("enter video time :")
            update_video(video_id,name,time)

        elif(choice=='4'):
            video_id=input("enter the video number to be updated :")
            delete_video(video_id)

        elif(choice=='5'):
            break

        else:
            print("please enter the valid choice !")
    
    connection.close()

if __name__=="__main__":
    main()