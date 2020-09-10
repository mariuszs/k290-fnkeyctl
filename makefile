CC = g++
CFLAGS = -std=gnu++0x
PREFIX = /usr/local

k290_fnkeyctl: k290_fnkeyctl.cpp
	${CC} ${CFLAGS} -g k290_fnkeyctl.cpp `pkg-config --libs libusb-1.0` -o k290_fnkeyctl

clean:
	rm k290_fnkeyctl

install: k290_fnkeyctl
	mkdir -p $(DESTDIR)$(PREFIX)/sbin
	install -m 755 -o root k290_fnkeyctl $(DESTDIR)$(PREFIX)/sbin/

.PHONY: uninstall
uninstall:
	rm -f $(DESTDIR)$(PREFIX)/sbin/k290_fnkeyctl
