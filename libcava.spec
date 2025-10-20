%global debug_package %{nil}

%define libname %mklibname cava
%define devname %mklibname cava -d

Name:           cava
Version:        0.10.4
Release:        2
Summary:        Fork to provide cava as a shared library, e.g. used by waybar. Cava is not provided as executable
Group:          System/Libraries
License:        MIT
URL:            https://github.com/LukashonakV/cava
Source0:        %{url}/archive/%version.tar.gz


BuildRequires:  iniparser-devel
BuildRequires:  fftw-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  portaudio-devel
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(sndio)
BuildRequires:  pkgconfig(jack)

Requires: cava

%description
%summary

%package -n %{libname}
Summary:    %{summary}
Group:      System/Libraries
Provides:   %{libname} = %{EVRD}

%description -n %{libname}
%summary

%package -n %{devname}
Summary:  Development files for %{name}
Group:    Development/C
Requires: %{libname} = %{EVRD}

%global __requires_exclude ^%{_libdir}/libastal\\.so*
%description -n %{devname}
Development files (Headers etc.) for %{name}.


%prep
%autosetup -p1

%build
meson setup --prefix /usr build
meson compile -C build
%install
%meson_install -C build
rm -rf %{buildroot}%{_datadir}/consolefonts/cava.psf


%files -n %{libname}
%license LICENSE
%doc README.md
%doc example_files
%{_libdir}/libcava.so

%files -n %{devname}
%{_includedir}/cava/util.h
%{_includedir}/cava/cavacore.h
%{_includedir}/cava/common.h
%{_includedir}/cava/config.h
%{_includedir}/cava/debug.h
%{_includedir}/cava/input/common.h
%{_includedir}/cava/input/jack.h
%{_includedir}/cava/output/common.h
%{_includedir}/cava/output/noritake.h
%{_includedir}/cava/output/raw.h
%{_includedir}/cava/output/sdl_cava.h
%{_includedir}/cava/output/sdl_glsl.h
%{_includedir}/cava/output/terminal_ncurses.h
%{_includedir}/cava/output/terminal_noncurses.h
%{_includedir}/cava/output/terminal_bcircle.h
%{_libdir}/pkgconfig/cava.pc




