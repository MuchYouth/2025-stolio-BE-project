from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship

from database import Base

# ManyToMany 관계를 적용
question_voter = Table(
    'question_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('question_id', Integer, ForeignKey('question.id'), primary_key=True)
)
answer_voter = Table(
    'answer_voter',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('answer_id', Integer, ForeignKey('answer.id'), primary_key=True)
)
class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    # User 모델을 Question 모델과 연결하기 위한 속성
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    # Question 모델에서 User 모델을 참조하기 위한 속성
    user = relationship("User", backref="question_users")
    modify_date = Column(DateTime, nullable=True)
    # secondary 값 :  Question 모델을 통해 추천인을 저장하면 실제 데이터는 question_voter 테이블에 저장되고 저장된 추천인 정보는 Question 모델의 voter 속성을 통해 참조
    # backref : 어떤 계정이 a_user 라는 객체로 참조되었다면 a_user.question_voters 으로 해당 계정이 추천한 질문 리스트를 구할수 있다.
    voter = relationship('User', secondary=question_voter, backref='question_voters')
class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    question_id = Column(Integer, ForeignKey("question.id"))
    question = relationship("Question", backref="answers")
    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref="answer_users")
    modify_date = Column(DateTime, nullable=True)
    voter = relationship('User', secondary=answer_voter, backref='answer_voters')
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)