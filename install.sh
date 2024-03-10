cd ./scripts

echo "Removing old dependencies..."
rm -rf ./node_modules

echo "Installing new dependencies..."
mkdir ./node_modules
cd ./node_modules

# HTMX
curl https://unpkg.com/htmx.org@1.9.10/dist/htmx.min.js -o ./htmx.min.js

pip install flask
# pip install Jinja2

echo "Done!"
