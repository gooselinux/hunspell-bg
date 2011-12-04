Name: hunspell-bg
Summary: Bulgarian hunspell dictionaries
Version: 4.1
Release: 5.1%{?dist}
Source: http://downloads.sourceforge.net/bgoffice/OOo-spell-bg-%{version}.zip
Group: Applications/Text
URL: http://bgoffice.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch

Requires: hunspell

%description
Bulgarian hunspell dictionaries.

%prep
%setup -q -n OOo-spell-bg-%{version}

%build
for i in README COPYING; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

iconv -f WINDOWS-1251 -t UTF-8 bg_BG.dic > bg_BG.dic.new
mv -f bg_BG.dic.new bg_BG.dic
echo "SET UTF-8" > bg_BG.aff.new
tail -n +2 bg_BG.aff | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> bg_BG.aff.new
mv bg_BG.aff.new bg_BG.aff

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.BULGARIAN README  
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 4.1-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Caolan McNamara <caolanm@redhat.com> - 4.1-4
- clean up spec

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Apr 21 2008 Caolan McNamara <caolanm@redhat.com> - 4.1-2
- rhbz#443297 recode .aff and .dic into UTF-8

* Tue Dec 18 2007 Caolan McNamara <caolanm@redhat.com> - 4.1-1
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 4.0-2
- clarify license, can't see a specific GPL version

* Mon Jul 09 2007 Caolan McNamara <caolanm@redhat.com> - 4.0-1
- latest version

* Mon Feb 12 2006 Caolan McNamara <caolanm@redhat.com> - 0.20040405-1
- initial version
