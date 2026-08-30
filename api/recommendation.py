from http.server import BaseHTTPRequestHandler
import json


def generate_recommendation(asset_type, temperature, risk):

    asset_type = asset_type or "Public Asset"

    if risk == "Extreme":
        return (
            f"URGENT: The {asset_type} is exposed to extreme heat "
            f"at {temperature:.2f}°C. Immediately provide shade, "
            "drinking-water access, and temporary heat-safety measures. "
            "Prioritize this location for urgent inspection."
        )

    if risk == "High":

        if asset_type == "Bus Stop":
            return (
                f"The {asset_type} is experiencing high heat "
                f"({temperature:.2f}°C). Install or improve a shaded "
                "shelter, provide drinking-water access, and prioritize "
                "this stop for heat-safety inspection."
            )

        if asset_type == "Playground":
            return (
                f"The {asset_type} is experiencing high heat "
                f"({temperature:.2f}°C). Increase shade coverage, "
                "provide drinking-water access, and inspect play "
                "surfaces during peak afternoon heat."
            )

        if asset_type == "Park":
            return (
                f"The {asset_type} is experiencing high heat "
                f"({temperature:.2f}°C). Increase shaded areas, "
                "provide drinking-water access, and prioritize "
                "heat-safe public amenities."
            )

        return (
            f"The {asset_type} is experiencing high heat "
            f"({temperature:.2f}°C). Prioritize this asset for heat "
            "mitigation by increasing shade, providing cooling or "
            "water access, and scheduling a heat-safety inspection."
        )

    if risk == "Moderate":
        return (
            f"The {asset_type} is experiencing moderate heat "
            f"({temperature:.2f}°C). Consider additional shade, "
            "drinking-water access, and routine monitoring during "
            "periods of high heat."
        )

    return (
        f"The {asset_type} is currently at a lower heat-risk level "
        f"({temperature:.2f}°C). Continue routine monitoring and "
        "maintain existing heat-safety measures."
    )


class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):

        self.send_response(204)

        self.send_header(
            "Access-Control-Allow-Origin",
            "*"
        )

        self.send_header(
            "Access-Control-Allow-Methods",
            "POST, OPTIONS"
        )

        self.send_header(
            "Access-Control-Allow-Headers",
            "Content-Type"
        )

        self.end_headers()


    def do_POST(self):

        if self.path != "/api/recommendation":
            self.send_response(404)
            self.end_headers()
            return

        try:

            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)

            data = json.loads(
                body.decode("utf-8")
            )

            asset_type = data.get(
                "asset_type",
                "Public Asset"
            )

            temperature = float(
                data.get("temperature", 0)
            )

            risk = data.get(
                "risk",
                "Unknown"
            )

            recommendation = generate_recommendation(
                asset_type,
                temperature,
                risk
            )

            response = {
                "success": True,
                "recommendation": recommendation
            }

            response_bytes = json.dumps(
                response
            ).encode("utf-8")

            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )

            self.send_header(
                "Access-Control-Allow-Methods",
                "POST, OPTIONS"
            )

            self.send_header(
                "Access-Control-Allow-Headers",
                "Content-Type"
            )

            self.end_headers()

            self.wfile.write(
                response_bytes
            )

        except Exception as error:

            response = {
                "success": False,
                "error": str(error)
            }

            response_bytes = json.dumps(
                response
            ).encode("utf-8")

            self.send_response(400)

            self.send_header(
                "Content-Type",
                "application/json"
            )

            self.send_header(
                "Access-Control-Allow-Origin",
                "*"
            )

            self.send_header(
                "Access-Control-Allow-Methods",
                "POST, OPTIONS"
            )

            self.send_header(
                "Access-Control-Allow-Headers",
                "Content-Type"
            )

            self.end_headers()

            self.wfile.write(
                response_bytes
            )
