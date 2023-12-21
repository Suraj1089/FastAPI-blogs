from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from sqladmin import Admin, ModelView

from api.v1.endpoints import converter, user, blog
from db.database import Base, engine
from db.models.blog import Post, Comment, Like
from db.models.user import User, Author


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="fastapi-tutorials",
    description="fastapi-tutorials"
)


# register fastapi admin panel
admin: Admin = Admin(app=app, engine=engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.email]


class PostAdmin(ModelView, model=Post):
    column_list = [User.id, User.email, User.email]


class CommentAdmin(ModelView, model=Comment):
    column_list = [Comment.id, Comment.content]


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, User.id]


class LikeAdmin(ModelView, model=Like):
    column_list = [Like.id, Like.like_count]


admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(CommentAdmin)
admin.add_view(LikeAdmin)

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(converter.router)


@app.get("/")
async def home():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
