Summary:	TCP proxy with load balancing
Summary(pl.UTF-8):	Proxy TCP z load balancingiem
Name:		proxylb
Version:	1.0.3
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.modperldev.com/projects/proxylb/%{name}-%{version}.tar.bz2
# Source0-md5:	5f5551bfd265392e6e1044d40c751a6a
Patch0:		%{name}-path.patch
URL:		http://www.modperldev.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Proxy load balance is a C program written to balance incoming
connections to numerous end boxes (computers) using a simple weight
algorithm. With its low memory and disk footprint, threads, it is
ideal for professional load balancing.

%description -l pl.UTF-8
Proxylb jest programem napisanym w C, służącym do rozkładania
obciążenia połączeń przychodzących przy użyciu prostego algorytmu.
Dzięki niskiemu zużyciu pamięci i miejsca na dysku, proxylb jest
idealnym narzędziem do profesjonalnego load balancingu.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install proxylb $RPM_BUILD_ROOT%{_bindir}
install config.txt $RPM_BUILD_ROOT%{_sysconfdir}/proxylb.conf
install proxy.filters_example $RPM_BUILD_ROOT%{_sysconfdir}/proxy.filters

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG TODO
%attr(755,root,root) %{_bindir}/proxylb
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/proxylb.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/proxy.filters
