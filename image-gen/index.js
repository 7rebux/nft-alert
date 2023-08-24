const nodeHtmlToImage = require("node-html-to-image");
const fs = require("fs");

if (!process.argv[2]) throw new Error("Missing image");
if (!process.argv[3]) throw new Error("Missing data");

const html = fs.readFileSync("./template.html");
const image = fs.readFileSync(process.argv[2]);
const base64Image = new Buffer.from(image).toString("base64");
const dataURI = "data:image/png;base64," + base64Image;
const data = JSON.parse(fs.readFileSync(process.argv[3]));

nodeHtmlToImage({
  output: "./result.png",
  selector: "#main",
  html: `<html><body>${html}</body></html>`,
  content: {
    title: data.title,
    number: data.number,
    image: dataURI,
    price1: data.price1,
    price2: data.price2,
    position: data.position,
    total: data.total,
    sold: data.sold,
  },
}).then(() => console.log("The image was created successfully!"));
