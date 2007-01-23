Summary:	A High Quality Rendering Engine for C++
Name:		agg
Version:	2.5
Release:	0.1
License:	GPL v2+
Group:		Libraries
URL:		http://www.antigrain.com/
Source0:	http://www.antigrain.com/%{name}-%{version}.tar.gz
# Source0-md5:	ddc67cbdc7d51e1ec984c2ac2724c08a
Patch0:		%{name}-depends.patch
BuildRequires:	SDL-devel
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anti-Grain Geometry (AGG) is a general purpose graphical toolkit
written completely in standard and platform independent C++. It can be
used in many areas of computer programming where high quality 2D
graphics is an essential part of the project.

AGG uses only C++ and standard C runtime functions, such as memcpy,
sin, cos, sqrt, etc. The basic algorithms don't even use C++ Standard
Template Library. Thus, AGG can be used in a very large number of
applications, including embedded systems.

%package devel
Summary:	Support files necessary to compile applications with agg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Libraries, headers, and support files necessary to compile
applications using agg

%package static
Summary:	Static agg library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static agg library.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__libtoolize}
%{__automake}
%configure \
	--disable-gpc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc authors copying readme
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/agg2
%{_pkgconfigdir}/libagg.pc
%{_aclocaldir}/libagg.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
