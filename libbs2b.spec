Summary:	Bauer stereophonic-to-binaural DSP library
Summary(pl.UTF-8):	Biblioteka DSP stereofoniczno-dwuusznego Bauera
Name:		libbs2b
Version:	3.1.0
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/bs2b/%{name}-%{version}.tar.lzma
# Source0-md5:	00d32ffa6461dde6a632c846da3e0a13
Patch0:		%{name}-format.patch
URL:		http://bs2b.sourceforge.net/
BuildRequires:	libsndfile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Bauer stereophonic-to-binaural DSP (bs2b) is designed to improve
headphone listening of stereo audio records.

%description -l pl.UTF-8
Stereofoniczno-dwuuszny DSP Bauera (bs2b) służy do poprawiania jakości
dźwiękowych nagrań stereofonicznych przez słuchawki.

%package devel
Summary:	Header files for bs2b library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki bs2b
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for bs2b library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki bs2b.

%package static
Summary:	Static bs2b library
Summary(pl.UTF-8):	Statyczna biblioteka bs2b
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static bs2b library.

%description static -l pl.UTF-8
Statyczna biblioteka bs2b.

%prep
%setup -q
%patch -P0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libbs2b.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/bs2bconvert
%attr(755,root,root) %{_bindir}/bs2bstream
%attr(755,root,root) %{_libdir}/libbs2b.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbs2b.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbs2b.so
%{_includedir}/bs2b
%{_pkgconfigdir}/libbs2b.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libbs2b.a
