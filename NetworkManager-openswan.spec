Summary:	NetworkManager VPN integration for openswan
Summary(pl.UTF-8):	Integracja NetworkManagera z openswan
Name:		NetworkManager-openswan
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openswan/1.0/%{name}-%{version}.tar.xz
# Source0-md5:	2294c870a370e61ba1fa58149d89aa4c
Patch0:		%{name}-symlink.patch
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel >= 2:1.0.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.0.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libnl-devel >= 3.2.8
BuildRequires:	libsecret-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.0.0
Requires:	dbus-glib >= 0.74
Requires:	gtk+3 >= 3.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for openswan.

%description -l pl.UTF-8
Integracja NetworkManagera z openswan.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-more-warnings \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-openswan

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-openswan.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openswan-properties.so
%attr(755,root,root) %{_libdir}/nm-libreswan-service-helper
%attr(755,root,root) %{_libdir}/nm-openswan-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openswan-service
%attr(755,root,root) %{_libdir}/nm-openswan-service-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openswan-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-openswan-service.conf
%dir %{_datadir}/gnome-vpn-properties/openswan
%{_datadir}/gnome-vpn-properties/openswan/nm-openswan-dialog.ui
%{_desktopdir}/nm-openswan-auth-dialog.desktop
