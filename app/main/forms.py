from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Required,Length,Email,EqualTo

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('product', 'product'), ('idea', 'idea'), ('business', 'business')],
                           validators=[Required()])
    submit = SubmitField('Post')
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Post')
class Vote(FlaskForm):
    submit = SelectField('Like')