Name:           libfido2

Version:        1.3.1
Release:        1%{?dist}
Summary:        FIDO2 library

License:        BSD
URL:            https://github.com/Yubico/%{name}
Source0:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz
Source1:        https://developers.yubico.com/%{name}/Releases/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-1D7308B0055F5AEF36944A8F27A9C24D9588EA0F.gpg

BuildRequires:  cmake
BuildRequires:  hidapi-devel
BuildRequires:  libcbor-devel
BuildRequires:  libudev-devel
BuildRequires:  openssl-devel
BuildRequires:  gcc
BuildRequires:  gnupg2
Requires:       u2f-hidraw-policy

%description
%{name} is an open source library to support the FIDO2 protocol.  FIDO2 is
an open authentication standard that consists of the W3C Web Authentication
specification (WebAuthn API), and the Client to Authentication Protocol
(CTAP).  CTAP is an application layer protocol used for communication
between a client (browser) or a platform (operating system) with an external
authentication device (for example the Yubico Security Key).

################################################################################

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{name}-devel contains development libraries and header files for %{name}.

################################################################################

%package -n fido2-tools

Summary:        FIDO2 tools
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n fido2-tools
FIDO2 command line tools to access and configure a FIDO2 compliant
authentication device.

################################################################################


%prep
gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -p1 -n %{name}-%{version}


%build
mkdir build
cd build
%cmake ..
%make_build


%install
%make_install -C build
# Remove static files per packaging guidelines
find %{buildroot} -type f -name "*.a" -delete -print


%files
%doc NEWS README.adoc
%license LICENSE
%{_libdir}/libfido2.so.1{,.*}

%files devel
%{_libdir}/pkgconfig/*
%{_libdir}/libfido2.so
%{_includedir}/*
%{_mandir}/man3/*

%files -n fido2-tools
%{_bindir}/*
%{_mandir}/man1/*


%changelog

* Thu Feb 20 2020 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.3.1-1
- 1.3.1 release

* Mon Dec 16 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.3.0-3
- use yubico corp release site for sources and gpg signature

* Sat Dec 14 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.3.0-2
- packaging cleanups

* Sat Nov 30 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.3.0-1
- 1.3.0 release

* Mon Jul 29 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.2.0-1
- 1.2.0 release

* Sat May 11 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.1.0-1
- 1.1.0 release

* Fri Apr 05 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.0.0-2
- include backported upstream patches for compiler dependencies and soname version
- modify libdir glob to meet newer packaging recommendations

* Thu Mar 21 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 1.0.0-1
- 1.0.0 release

* Mon Jan 07 2019 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.4.0-1
- 0.4.0 release

* Wed Sep 12 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-1
- 0.3.0 release

* Fri Sep 07 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.8.20180907git878fcd8
- update to upstream master

* Thu Sep 06 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.7.20180906gitff7ece8
- update to upstream master

* Wed Sep 05 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.6.20180905gitcb4951c
- update to upstream master

* Tue Sep 04 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.5.20180904git2b5f0d0
- update to upstream master

* Mon Aug 27 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.4.20180827git9d178b2
- Update to upstream master

* Thu Aug 23 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.3.20180823git0f40181
- Update to upstream master

* Tue Aug 21 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.2.20180821gitfff65a4
- Update to upstream master

* Wed Aug 08 2018 Gary Buhrmaster <gary.buhrmaster@gmail.com> 0.3.0-0.1.20180808git5be8903
- Update to new spec

