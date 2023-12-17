from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from sqladmin import Admin, ModelView

from api.v1.endpoints import converter, user, blog
from db.database import Base, engine
from db.models.blog import Post, Comment
from db.models.user import User, Author

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

Base.metadata.create_all(bind=engine)

app = FastAPI()

# register fastapi admin panel
admin = Admin(app=app, engine=engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.email]


class PostAdmin(ModelView, model=Post):
    column_list = [User.id, User.email, User.email]


class CommentAdmin(ModelView, model=Comment):
    column_list = [Comment.id, Comment.content]


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, User.id]


admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(CommentAdmin)

app.include_router(user.router)
app.include_router(blog.router)
app.include_router(converter.router)


@app.get("/")
async def home():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
