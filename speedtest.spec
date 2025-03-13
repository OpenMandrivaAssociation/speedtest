%global rdnsappid xyz.ketok.Speedtest

Name:           speedtest
Version:        1.4.0
Release:        1
Summary:        A graphical librespeed client written using gtk4 + libadwaita
License:        GPL-3.0-or-later
URL:            https://github.com/Ketok4321/speedtest
Source0:        https://github.com/Ketok4321/speedtest/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  blueprint-compiler >= 0.10.0
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  appstream-util
BuildRequires:  meson >= 0.62.0
BuildRequires:  pkgconfig(python3)

BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(aiohttp)

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       hicolor-icon-theme
Requires:       libadwaita-common
Requires:       python-gobject3
Requires:       python-gi
Requires:       gtk4
Requires:       python3dist(aiohttp)

%description
%{summary}


%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}


%files -f %{name}.lang
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
