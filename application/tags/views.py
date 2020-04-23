from application import app, db

from application.tags.models import Tag

from flask import request, render_template

@app.route('/tags/', methods=['GET'])
def list_tags():
    tags = Tag.query.all()
    mostTips = None
    mostLikes = None

    for tag in tags:
        if not mostTips or len(tag.tips) > len(mostTips.tips):
            mostTips = tag

        likes = 0

        mostLiked = None
        for tip in tag.tips:
            likes = likes + tip.likes
            if not mostLiked or tip.likes > mostLiked.likes:
                mostLiked = tip
        tag.mostLiked = mostLiked

        if not mostLikes or likes > mostLikes.likes:
            mostLikes = tag
            mostLikes.likes = likes

    
    return render_template('tags/list.html', tags = tags, mostTips = mostTips, mostLikes = mostLikes)