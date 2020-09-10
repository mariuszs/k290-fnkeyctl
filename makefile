CC = g++
CFLAGS = -std=gnu++0x

k290_fnkeyctl: k290_fnkeyctl.cpp
	${CC} ${CFLAGS} k290_fnkeyctl.cpp `pkg-config --libs libusb-1.0` -o k290_fnkeyctl
