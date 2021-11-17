OUTPUT=app
CFLAGS=-Wall -g -fsanitize=address

%:%.c mymalloc.h
		gcc $(CFLAGS) -o $@ $^

all: ls.c find.c tree.c
		gcc $(CFLAGS) -o $@ $^
