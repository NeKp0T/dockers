FROM ubuntu

ADD /add/* /exec/
ENTRYPOINT ["/exec/script.sh"]