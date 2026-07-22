from playwright.sync_api import sync_playwright, expect

def test_verify_all_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        expect(page).to_have_title("Automation Exercise")
        page.get_by_role("link", name="Products").click()
        expect(page).to_have_title("Automation Exercise - All Products")
        # 5. Verify user is navigated to ALL PRODUCTS page successfully
        expect(page.get_by_text("All Products")).to_be_visible()

        # 6. The products list is visible
        expect(page.locator(".features_items")).to_be_visible()
        expect(page.locator(".product-image-wrapper").first).to_be_visible()

        page.locator('a[href="/product_details/1"]').click()
        expect(page).to_have_title("Automation Exercise - Product Details")

        product_information = page.locator(".product-information")

        expect(product_information).to_be_visible()
        #Lembre de usar to_be_visible para conferir e identifique a função do que quer buscar
        expect(product_information.locator("h2")).to_be_visible()
        expect(product_information.locator("span span")).to_be_visible()
        #Linhas com <p> são muito genéricas, você tem que filtrar.
        expect(product_information.locator("p").filter(has_text="Category:")).to_be_visible()
        expect(product_information.locator("p").filter(has_text="Availability:")).to_be_visible()
        expect(product_information.locator("p").filter(has_text="Condition:")).to_be_visible()
        expect(product_information.locator("p").filter(has_text="Brand:")).to_be_visible()

        #outro exemplo para o mesmo problema
        #expect(product_information).to_be_visible()
        #expect(product_information.locator("h2")).to_be_visible()
        #expect(product_information.get_by_text("Category:")).to_be_visible()
        #expect(product_information.locator("span span")).to_be_visible()
        #expect(product_information.get_by_text("Availability:")).to_be_visible()
        #expect(product_information.get_by_text("Condition:")).to_be_visible()
        #expect(product_information.get_by_text("Brand:")).to_be_visible()


        browser.close()