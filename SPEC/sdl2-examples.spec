Name:           sdl2-examples
Version:        1.0
Release:        alt1
Summary:        SDL2 Grumpy Cat Demo
License:        BSD-3
URL:            https://github.com/xyproto/sdl2-examples.git
Source0:        %{name}-%{version}.tar
Group:          Development/Other
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libSDL2-devel
BuildRequires:  desktop-file-utils

%description
Implementation of Grumpy Cat demo using SDL2.

%prep
%setup -q

%build
for std in 11 14 17 20; do
  mkdir -p build-cpp${std}
  cmake -S c++${std}-cmake -B build-cpp${std} \
        -DCMAKE_BUILD_TYPE=3.23.2 \
        -DCMAKE_CXX_STANDARD=${std} \
        -DIMGDIR="%{_datadir}/%{name}/img"
  make -C build-cpp${std} %{?_smp_mflags}
done

%install
install -m 0755 -d %{buildroot}/%{_bindir}
for std in 11 14 17 20; do
  install -m 0755 build-cpp${std}/main %{buildroot}/%{_bindir}/grumpycat-cpp${std}
done


install -m 0755 -d %{buildroot}/%{_datadir}/%{name}/img
install -m 0644 img/grumpy-cat.bmp %{buildroot}/%{_datadir}/%{name}/img/
install -m 0644 img/grumpy-cat.png %{buildroot}/%{_datadir}/%{name}/img/


install -m 0755 -d %{buildroot}/%{_datadir}/applications
for std in 11 14 17 20; do
  cat > %{buildroot}/%{_datadir}/applications/grumpycat-cpp${std}.desktop <<EOF
[Desktop Entry]
Version=1.0
Name=Grumpy Cat (C++${std})
Comment=SDL2 Grumpy Cat Demo
Exec=grumpycat-cpp${std}
Icon=%{_datadir}/%{name}/img/grumpy-cat.png
Terminal=false
Type=Application
Categories=Graphics;Game;
EOF
done

%post
touch --no-create %{_datadir}/applications/*.desktop || :
update-desktop-database %{_datadir}/applications || :

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/applications || :
  update-desktop-database %{_datadir}/applications || :
fi

%files
%{_bindir}/grumpycat-cpp*
%{_datadir}/%{name}/img/*
%{_datadir}/applications/grumpycat-cpp*.desktop
%doc README.md
%doc LICENSE
%doc COMPILES.md

%changelog
* Mon Apr 29 2025 Mikhail Sokolov <msok15@mail.ru> - 1.0-alt1
- Initial package
- Added desktop files for menu integration
- Added post-install scripts for desktop database update
