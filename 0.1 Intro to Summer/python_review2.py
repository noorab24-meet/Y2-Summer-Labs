def create_youtube_video(title, description):
    video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return video

def like(video):
    if "likes" in video:
        video["likes"] += 1
    return video

def dislike(video):
    if "dislikes" in video:
        video["dislikes"] += 1
    return video

def add_comment(youtubevideo, username, comment_text):
    youtubevideo.setdefault("comments", {})[username] = comment_text
    return youtubevideo

video1 = create_youtube_video("Introduction to Python", "A beginner's guide to Python programming")
print("Initial Video Dictionary:")
print(video1)
print()














