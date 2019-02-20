from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def functional_test():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://127.0.0.1:5000/')

    start_point = driver.find_element_by_id('start_point')
    start_point.click()

    land_point = driver.find_element_by_id('land_point')
    land_point.click()

    draw_line = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/a/div')
    draw_line.click()

    markers = driver.find_elements_by_class_name('leaflet-marker-icon')

    for marker in markers:
        alt = marker.get_attribute('alt')
        if alt == 'startPoint':
            start_marker = marker
        if alt == 'landPoint':
            land_marker = marker

    # Click on start point
    click_start_action = webdriver.common.action_chains.ActionChains(driver)
    click_start_action.move_to_element_with_offset(start_marker, 0, 41)
    click_start_action.click()
    click_start_action.perform()

    # Click on others points
    land_marker.click()

    # Click on land point
    click_land_action = webdriver.common.action_chains.ActionChains(driver)
    click_land_action.move_to_element_with_offset(land_marker, 0, 41)
    click_land_action.click()
    click_land_action.perform()

    finish_button = driver.find_element_by_class_name('action-finish')
    finish_button.click()

    # Export track
    driver.find_element_by_id('export').click()

if __name__ == '__main__':
    functional_test()
