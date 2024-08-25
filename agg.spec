Summary:	A High Quality Rendering Engine for C++
Summary(pl.UTF-8):	Silnik renderujący wysokiej jakości dla C++
Name:		agg
Version:	2.5
Release:	8
License:	GPL v2+
Group:		Libraries
Source0:	http://www.antigrain.com/%{name}-%{version}.tar.gz
# Source0-md5:	ddc67cbdc7d51e1ec984c2ac2724c08a
Patch0:		%{name}-depends.patch
Patch1:		ac.patch
Patch2:		cxx.patch
Patch3:		%{name}-types.patch
URL:		http://www.antigrain.com/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Unresolved symbol: _Z8agg_mainiPPc
%define		skip_post_check_so	libaggplatformsdl.so.*.*.* libaggplatformX11.so.*.*.* libaggplatformsdl.so.*.*.*

%description
Anti-Grain Geometry (AGG) is a general purpose graphical toolkit
written completely in standard and platform independent C++. It can be
used in many areas of computer programming where high quality 2D
graphics is an essential part of the project.

AGG uses only C++ and standard C runtime functions, such as memcpy,
sin, cos, sqrt, etc. The basic algorithms don't even use C++ Standard
Template Library. Thus, AGG can be used in a very large number of
applications, including embedded systems.

%description -l pl.UTF-8
Anti-Grain Geometry (AGG) to toolkit graficzny ogólnego przeznaczenia
napisany całkowicie w standardowym i niezależnym od platformy C++.
Może być używany w wielu zastosowaniach z zakresu programowania gdzie
zasadniczą częścią projektu jest wysokiej jakości grafika 2D.

AGG używa tylko C++ i standardowych funkcji C, takich jak memcpy, sin,
cos, sqrt itp. Podstawowe algorytmy nie używają nawet standardowej
biblioteki C++. W ten sposób AGG może być używany w bardzo wielu
zastosowaniach, także na systemach wbudowanych.

%package devel
Summary:	Support files necessary to compile applications with agg
Summary(pl.UTF-8):	Pliki potrzebne do kompilowania aplikacji z użyciem agg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
# libaggfontfreetype R: freetype-devel
# libaggplatformX11 R: xorg-lib-libX11-devel
# libaggplatformsdl R: SDL-devel

%description devel
Header and support files necessary to compile applications using agg.

%description devel -l pl.UTF-8
Pliki nagłówkowe i pomocnicze potrzebne do kompilowania aplikacji z
użyciem agg.

%package static
Summary:	Static agg library
Summary(pl.UTF-8):	Statyczna biblioteka agg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static agg library.

%description static -l pl.UTF-8
Statyczna biblioteka agg.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-gpc \
	--disable-examples

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc authors copying readme
%attr(755,root,root) %{_libdir}/libagg.so.*.*.*
%ghost %{_libdir}/libagg.so.2
%attr(755,root,root) %{_libdir}/libaggfontfreetype.so.*.*.*
%ghost %{_libdir}/libaggfontfreetype.so.2
%attr(755,root,root) %{_libdir}/libaggplatformX11.so.*.*.*
%ghost %{_libdir}/libaggplatformX11.so.2
%attr(755,root,root) %{_libdir}/libaggplatformsdl.so.*.*.*
%ghost %{_libdir}/libaggplatformsdl.so.2

%files devel
%defattr(644,root,root,755)
%{_libdir}/libagg.so
%{_libdir}/libaggfontfreetype.so
%{_libdir}/libaggplatformX11.so
%{_libdir}/libaggplatformsdl.so
%{_libdir}/libagg.la
%{_libdir}/libaggfontfreetype.la
%{_libdir}/libaggplatformX11.la
%{_libdir}/libaggplatformsdl.la
%{_includedir}/agg2
%{_pkgconfigdir}/libagg.pc
%{_aclocaldir}/libagg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libagg.a
%{_libdir}/libaggfontfreetype.a
%{_libdir}/libaggplatformX11.a
%{_libdir}/libaggplatformsdl.a
