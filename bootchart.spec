Summary:	A 'startup' graphing tool
Name:		bootchart
Version:	1.20
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://foo-projects.org/~sofar/bootchart/%{name}-%{version}.tar.gz
# Source0-md5:	071c67856a2b16e1a9e93a058de3eb65
URL:		https://github.com/sofar/bootchart
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bootchart is a tool, usually run at system startup, that collects and
graphs the CPU and disk load of the system as it works. The output of
bootchart is an SVG graph.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D bootchartd.conf.example \
	$RPM_BUILD_ROOT%{_sysconfdir}/bootchartd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_sbindir}/bootchartd
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/bootchartd.conf

