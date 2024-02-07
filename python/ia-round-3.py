pageSize = 10;
pageNumber = 3;

# SELECT *
# FROM accountStatement
# order by accountStatement.modifedAt DESC
# LIMIT pageSize OFFSET pageSize (10) * pageNumber -1 (2);




# Quora

# REQS
# Login
# Post QUESTION
# answer on any question
# Like a particular answer
# comment on a particular answer
# Logout

# user
# uid AI PK INT(20)

# question
# qId AI PK INT(20)
# userId FK INT(20)
# question varchar(500)
# createdAt DateTime
# modifiedAt DateTime


# answer
# aId AI PK INT(20)
# userId FK INT(20)
# questionId FK INT(20)
# answer varchar(500)
# likesCount INT(20) default 0
# createdAt DateTime
# modifiedAt DateTime

# comment
# cId AI PK INT(20)
# userId FK INT(20)
# answerId FK INT(20)
# comment varchar(500)
# createdAt DateTime
# modifiedAt DateTime

# likes
# lId
# answerId
# userId
