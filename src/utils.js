
// const HOST = ""
const HOST = "http://localhost:8081"

function prepUrl(url) {
	return HOST + url
}

export default {
	prepUrl: prepUrl
}
