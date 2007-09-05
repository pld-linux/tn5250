# TODO: python binding
Summary:	5250 Telnet protocol and Terminal
Summary(pl.UTF-8):	Obsługa protokołu i terminal Telnet 5250
Name:		tn5250
Version:	0.17.3
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/tn5250/%{name}-%{version}.tar.gz
# Source0-md5:	f8c454334c63ed7b100e0b12160d93ea
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-no_libnsl.patch
URL:		http://tn5250.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tn5250 is an implementation of the 5250 Telnet protocol. It provide
5250 library and 5250 terminal emulation.

%description -l pl.UTF-8
tn5250 to implementacja protokołu Telnet 5250. Zawiera bibliotekę 5250
i emulator terminala 5250.

%package devel
Summary:	Development tools for 5250 protocol
Summary(pl.UTF-8):	Pakiet dla programisty protokołu 5250
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel
Requires:	openssl-devel >= 0.9.7d

%description devel
Header files to use lib5250.

%description devel -l pl.UTF-8
Pliki nagłówkowe do korzystania z lib5250.

%package static
Summary:	Static libraries for 5250 protocol
Summary(pl.UTF-8):	Statyczne biblioteki do protokołu 5250
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libraries to use lib5250.

%description static -l pl.UTF-8
Statyczne biblioteki lib5250.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure
%{__make}

cd linux
tic 5250.terminfo -o .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D linux/5/5250 $RPM_BUILD_ROOT%{_datadir}/terminfo/5/5250
install -D linux/x/xterm-5250 $RPM_BUILD_ROOT%{_datadir}/terminfo/x/xterm-5250

mv -f linux/README README.linux

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README* TODO
%attr(755,root,root) %{_bindir}/*5250
%attr(755,root,root) %{_bindir}/lp5250d
%attr(755,root,root) %{_bindir}/scs2*
%attr(755,root,root) %{_libdir}/lib5250.so.*.*.*
%{_datadir}/%{name}
%{_datadir}/terminfo/5/*
%{_datadir}/terminfo/x/*
%{_mandir}/man[15]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tn5250-config
%attr(755,root,root) %{_libdir}/lib5250.so
%{_libdir}/lib5250.la
%{_includedir}/tn5250.h
%{_includedir}/tn5250
%{_aclocaldir}/tn5250.m4
%{_pkgconfigdir}/tn5250.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib5250.a
