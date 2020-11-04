FROM python:3

LABEL maintainer="laercio.serra@gmail.com"
LABEL version="1.0"
LABEL description="Challenge for Data Engineer at BOA"

# set a directory for the app
WORKDIR /home/lserra/PycharmProjects/challenge_boa

# copy all the files to the container
COPY . .

# install dependencies
RUN apt-get -yqq update
RUN pip install --no-cache-dir -r requirements.txt

# run the command
CMD ["bash"]
