.PHONY: all bonus clean fclean re

all:
	cp 101pong.py 101pong

bonus:
	cp bonus/pong.py bonus/pong
	chmod +x bonus/pong

clean:

fclean:
	rm -f 101pong bonus/pong

re: fclean all