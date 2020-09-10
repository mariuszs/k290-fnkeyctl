Name:           k290-fnkeyctl
Version:        1.2
Release:        1%{?dist}
Summary:        Configures the behaviour of the F-keys on the Logitech K290

License:        MIT
URL:            https://github.com/mariuszs/k290-fnkeyctl
Source0:        https://github.com/mariuszs/k290-fnkeyctl/archive/v1.2.tar.gz

BuildRequires:  libusbx-devel
BuildRequires:  gcc-c++

%description
Configures the behaviour of the F-keys on the Logitech K290

%prep
%setup -q

%build
./build.sh

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/local/sbin/
mkdir -p %{buildroot}/lib/udev/rules.d/

install -m 755 k290_fnkeyctl %{buildroot}/usr/local/sbin/
install -m 644 99-k290-config.rules %{buildroot}/lib/udev/rules.d/

%files
/usr/local/sbin/k290_fnkeyctl
/lib/udev/rules.d/99-k290-config.rules

%changelog
* Thu Sep 10 2020 Mariusz Smykula <mariuszs@gmail.com> 1.2-1
- new package built with tito

* Thu Nov  5 2015 Mariusz Smykuła
- Initial rpm version
