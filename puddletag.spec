Summary:        Feature rich, easy to use tag editor
Name:           puddletag
Version:        1.0.5
Release:        2
Group:          Sound
License:        GPLv2 and GPLv3+
URL:            https://puddletag.sourceforge.net
Source0:        https://downloads.sourceforge.net/project/puddletag/puddletag-%{version}.tar.gz
Patch0:         puddletag-0.10.6-xdg.patch
BuildArch:      noarch
BuildRequires:  python-setuptools
BuildRequires:  desktop-file-utils

%description
Puddletag is an audio tag editor.

Unlike most taggers, it uses a spreadsheet-like layout so that all the
tags you want to edit by hand are visible and easily editable.

The usual tag editor features are supported like extracting tag
information from filenames, renaming files based on their tags by
using patterns (that you define, not crappy, uneditable ones).

Then there're Functions, which can do things like replace text, trim,
change the case of tags, etc. Actions can automate repetitive
tasks. You can import your QuodLibet library, lookup tags using
MusicBrainz, FreeDB or Amazon (though it's only good for cover art)
and more.

Supported formats: ID3v1, ID3v2 (mp3), MP4 (mp4, m4a, etc.),
VorbisComments (ogg, flac), Musepack (mpc), Monkey's Audio (.ape) and
WavPack (wv).

%prep
%autosetup -p1
%{__chmod} 0644 NEWS
%{__sed} -i  '/^#![ ]*\/usr\/bin\/env/d' \
    puddlestuff/{webdb,puddlesettings,puddletag,puddleobjects,releasewidget}.py

find . -name "*.py" |xargs 2to3 -w

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
desktop-file-install --vendor="" \
		     --add-category="Utility" \
		     --dir %buildroot%_datadir/applications \
		     %buildroot%_datadir/applications/*.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc copyright HACKING NEWS README THANKS TODO 
%{_bindir}/%{name}
%_mandir/man1/%name.1*
%{python_sitelib}/puddlestuff/
%{python_sitelib}/%{name}-%{version}-py*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png



%changelog
* Mon Sep 03 2012 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdv2012.0
+ Revision: 816249
- fix desktop entry
- update to new version 1.0.1

* Fri Aug 24 2012 Götz Waschk <waschk@mandriva.org> 1.0.0-1
+ Revision: 815662
- new version
- fix desktop entry
- update file list

* Fri Aug 26 2011 Götz Waschk <waschk@mandriva.org> 0.10.6.3-1
+ Revision: 697162
- update to new version 0.10.6.3

* Wed Jun 08 2011 Götz Waschk <waschk@mandriva.org> 0.10.6-1
+ Revision: 683199
- new version
- rediff the patch
- add man page

* Tue Apr 26 2011 Götz Waschk <waschk@mandriva.org> 0.10.3-2
+ Revision: 659240
- reduce python-qt4 deps

* Sun Apr 24 2011 Götz Waschk <waschk@mandriva.org> 0.10.3-1
+ Revision: 658363
- import puddletag

