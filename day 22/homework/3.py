# ლექსიკონი მოსწავლეების და მათი საყვარელი სიმღერების შესანახად
favorite_songs = {
    "Ana": "Song A",
    "Giorgi": "Song B",
    "Mari": "Song A",
    "Luka": "Song C"
}

# მოსწავლეების შედარება
students = list(favorite_songs.keys())  # მოსწავლეების სია

for i in range(len(students)):
    for j in range(i + 1, len(students)):  
        student1 = students[i]
        student2 = students[j]
        
        if favorite_songs[student1] == favorite_songs[student2]:
            print(f"{student1} და {student2} - we have the same favorite song")
        else:
            print(f"{student1} და {student2} - we have different favorite songs")
