FROM ubuntu:14.04
MAINTAINER Codey Oxley
EXPOSE 5000
# Set following in environment
#   NIPAPD_AUTH
#   EMAIL_FROM
#   EMAIL_TO
#   NIPAPD
#   WELCOME_MSG
#   SMTP_SERVER
#   DEBUG
#   NIPAPD_PASS
#   NIPAPD_USER

ENV INI_FILE=/etc/nipap/nipap-www.ini
# Gather nipap-www from dist
RUN apt-get install -y curl \
                       python2.7
RUN echo "deb http://spritelink.github.io/NIPAP/repos/apt stable main extra" \
         > /etc/apt/sources.list.d/nipap.list
RUN curl -L https://spritelink.github.io/NIPAP/nipap.gpg.key | apt-key add -
RUN mkdir /etc/nipap
# Make sure installer only places .dist files, not replacing existing
RUN [ ! -f $INI_FILE ] && touch $INI_FILE; touch /rm_ini.txt
# RUN chattr +i $INI_FILE
RUN chmod a-w $INI_FILE
RUN apt-get update && flock -x /etc/nipap apt-get \
                      -o Dpkg::Options::="--force-confdef" \
                      -o Dpkg::Options::="--force-confold" \
                      install -y nipap-www
# RUN chattr -i $INI_FILE
RUN chmod a+w $INI_FILE
RUN [ -f /rm_ini.txt ] && rm /rm_ini.txt && rm /etc/nipap/nipap-www.ini
#

# Custom
COPY conf/nipap-www.wsgi /etc/nipap/
COPY conf/ /resources
COPY nipap_www_init.py /resources/

CMD bash -c 'python /resources/nipap_www_init.py && \
             paster serve /etc/nipap/nipap-www.ini'
