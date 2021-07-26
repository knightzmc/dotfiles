ln -sv "$(pwd)"/.local/bin/sftp_uploader ~/.local/bin/
ln -sv "$(pwd)"/.local/bin/config.ini ~/.local/bin/
ln -sv "$(pwd)"/.local/bin/screenshot ~/.local/bin
ln -sv "$(pwd)"/.local/bin/suntools.py ~/.local/bin
ln -sv "$(pwd)"/.zshrc ~

ln -sv "$(pwd)"/.i3/config ~/.i3

mkdir ~/.config/polybar
ln -sv /home/alex/dotfiles/.config/polybar/* ~/.config/polybar/

mkdir ~/.doom.d
ln -sv "$(pwd)"/.doom.d/* ~/.doom.d
