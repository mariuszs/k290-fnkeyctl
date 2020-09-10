Name:           k290-fnkeyctl
Version:        1.2.1
Release:        1%{?dist}
Summary:        Configures the behaviour of the F-keys on the Logitech K290

License:        MIT
URL:            https://github.com/mariuszs/k290-fnkeyctl

BuildRequires:  libusbx-devel
BuildRequires:  gcc-c++

Requires(post): info
Requires(preun): info

%description
Configures the behaviour of the F-keys on the Logitech K290

%prep
%setup -q

%build
make

%install
make DESTDIR=%{?buildroot} install
mkdir -p %{buildroot}/lib/udev/rules.d/

install -m 644 99-k290-config.rules %{buildroot}/lib/udev/rules.d/

%files
%{_bindir}/usr/local/sbin/k290_fnkeyctl
%{_bindir}/lib/udev/rules.d/99-k290-config.rules

%changelog
* Thu Nov  5 2015 Mariusz Smykuła
- Initial rpm version
