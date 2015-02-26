#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	SpeexDSP - speech processing library that goes along with the Speex codec
Summary(pl.UTF-8):	SpeexDSP - biblioteka do przetwarzania mowy towarzysząca kodekowi Speex
Name:		speexdsp
Version:	1.2
%define	subver	rc3
%define	rel	2
Release:	0.%{subver}.%{rel}
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	70d9d31184f7eb761192fd1ef0b73333
URL:		http://www.speex.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
Conflicts:	speex < 1.2-rc2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SpeexDSP is a speech processing library that goes along with the Speex
codec.

%description -l pl.UTF-8
SpeexDSP to biblioteka do przetwarzania mowy towarzysząca kodekowi
Speex.

%package devel
Summary:	SpeexDSP library - development files
Summary(pl.UTF-8):	Pliki dla programistów używających biblioteki SpeexDSP
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Conflicts:	speex-devel < 1.2-rc2

%description devel
SpeexDSP library - development files.

%description devel -l pl.UTF-8
Pliki dla programistów używających biblioteki SpeexDSP.

%package static
Summary:	SpeexDSP static library
Summary(pl.UTF-8):	Biblioteka statyczna SpeexDSP
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Conflicts:	speex-static < 1.2-rc2

%description static
SpeexDSP static library.

%description static -l pl.UTF-8
Biblioteka statyczna SpeexDSP.

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	doc_DATA=

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libspeexdsp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libspeexdsp.so.1

%files devel
%defattr(644,root,root,755)
%doc doc/manual.pdf
%attr(755,root,root) %{_libdir}/libspeexdsp.so
%{_libdir}/libspeexdsp.la
# note: dir shared with speex-devel
%dir %{_includedir}/speex
%{_includedir}/speex/speex_echo.h
%{_includedir}/speex/speex_jitter.h
%{_includedir}/speex/speex_preprocess.h
%{_includedir}/speex/speex_resampler.h
%{_includedir}/speex/speexdsp_*.h
%{_pkgconfigdir}/speexdsp.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libspeexdsp.a
%endif
