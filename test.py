import unittest
from quart import Quart
from main import app

class LiteratureAppTestCase(unittest.IsolatedAsyncioTestCase):
    async def setUp(self):
        self.app = app.test_client()

    async def test_list_all(self):
        response = await self.app.post("/list_all/5/ukr")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("list all", data)
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_get_books(self):
        response = await self.app.post("/get_books/5/ukr/John Doe/")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("books", data)
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_get_presentation(self):
        response = await self.app.post("/get_presentation/5/ukr")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_get_bio(self):
        response = await self.app.post("/get_bio/5/ukr/John Doe")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_get_content(self):
        response = await self.app.post("/get_content/5/ukr/John Doe/Book Title")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_get_rnd(self):
        response = await self.app.post("/get_rnd/5/ukr")
        self.assertEqual(response.status_code, 200)
        data = await response.get_json()
        self.assertIn("Main web-site view eng", data)
        self.assertIn("Main web-site view ukr", data)

    async def test_plugin_logo(self):
        response = await self.app.get("/logo.jpg")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "image/png")

    async def test_plugin_manifest(self):
        response = await self.app.get("/.well-known/ai-plugin.json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

    async def test_openapi_spec(self):
        response = await self.app.get("/openapi.yaml")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "text/yaml")

if __name__ == "__main__":
    unittest.main()
