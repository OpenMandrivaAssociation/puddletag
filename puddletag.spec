%define pyqt 4.5
Summary:        Feature rich, easy to use tag editor
Name:           puddletag
Version:        0.10.6
Release:        %mkrel 1
Group:          Sound
License:        GPLv2 and GPLv3+
URL:            http://puddletag.sourceforge.net
Source0:        http://downloads.sourceforge.net/puddletag/puddletag-%{version}.tar.gz
Patch0:         puddletag-0.10.6-xdg.patch
BuildArch:      noarch
BuildRequires:  python-setuptools
Buildrequires:  desktop-file-utils
# Dependencies on Python modules are not automatic yet.
Requires:       python-qt4-gui >= %pyqt
Requires:       python-qt4-svg >= %pyqt
Requires:       python-parsing >= 1.5.1
Requires:       mutagen
Requires:       python-imaging
Requires:       python-configobj
Requires:       python-musicbrainz2 
#Requires:       quodlibet

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
%setup -q
%patch0 -p1
%{__chmod} 0644 NEWS
%{__sed} -i  '/^#![ ]*\/usr\/bin\/env/d' \
    puddlestuff/{webdb,puddlesettings,puddletag,puddleobjects,releasewidget}.py

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

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
%{_datadir}/pixmaps/%{name}.xpm

