FROM alpine
COPY ["flaskvj","."]
RUN apk add --update \
	bash \
	python \
	python-dev \
	py-pip \
	build-base \
	&& pip install requests \
	&& pip install flask \
	&& pip install bs4
CMD	python main.py