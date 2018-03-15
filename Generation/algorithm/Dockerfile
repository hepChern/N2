##
## A container where CernVM-FS is up and running
##
FROM rootproject/root-ubuntu16

USER root
ENV USER root
ENV HOME /root
WORKDIR /root

ADD .chern/mkdir.sh mkdir.sh
ADD .chern/check_output.sh check_output.sh
RUN bash ./mkdir.sh

# ===================================================================
# !! Please only modify the contents between the two seperation line

# Add all the code you use to docker image
ADD main.C $HOME/main.C

ENTRYPOINT ["root", "-b", "-q", "test.C"]
# other examples:
# ENTRYPOINT ["python", "-b", "-q", "test2.C"]

# ===================================================================
CMD ["bash", "check_output.sh"]

