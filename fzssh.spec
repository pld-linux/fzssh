Summary:	SSH/SFTP library based on libfilezilla
Summary(pl.UTF-8):	Biblioteka SSH/SFTP bazująca na libfilezilla
Name:		fzssh
Version:	1.2.0
Release:	1
License:	AGPLv3+
Group:		Libraries
#Source0-dl:	https://fzssh.filezilla-project.org/download.php
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	216310b4d9bc9ee8b272f4a57ef3076a
URL:		https://fzssh.filezilla-project.org/
BuildRequires:	gmp-devel >= 6.2
BuildRequires:	libargon2-devel
BuildRequires:	libfilezilla-devel >= 0.55.4
BuildRequires:	meson
BuildRequires:	nettle-devel >= 3.10
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.583
Requires:	gmp >= 6.2
Requires:	libargon2
Requires:	libfilezilla >= 0.55.4
Requires:	nettle >= 3.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
fzssh is a SSH/SFTP library based on libfilezilla

This library is free software, it is distributed under the terms and
conditions of the GNU Affero General Public License v3+ with
attribution, see the library's README file for details.

fzssh is a cross-platform library for all major operating systems,
including but not limited to Linux, *BSD, macOS and Windows.

%description -l pl.UTF-8
fzssh to biblioteka SSH/SFTP oparta na libfilezilla.

Ta biblioteka jest wolnym oprogramowaniem, rozpowszechnianym na
warunkach licencji GNU Affero General Public License v3+ z uznaniem
autorstwa. Szczegółowe informacje znajdują się w pliku README
biblioteki.

fzssh to biblioteka wieloplatformowa dla wszystkich głównych systemów
operacyjnych, w tym między innymi Linuxa, *BSD, macOS i Windowsa.

%package devel
Summary:	Header files for fzssh library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki fzssh
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel >= 6.2
Requires:	libargon2-devel
Requires:	libfilezilla-devel >= 0.55.3
Requires:	nettle-devel >= 3.10

%description devel
Header files for libfilezilla library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfilezilla.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README
%{_libdir}/libfzssh-client.so.*.*.*
%{_libdir}/libfzssh-crypt.so.*.*.*
%{_libdir}/libfzssh.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libfzssh-client.so
%{_libdir}/libfzssh-crypt.so
%{_libdir}/libfzssh.so
%{_includedir}/fzssh
%{_pkgconfigdir}/libfzssh-client.pc
