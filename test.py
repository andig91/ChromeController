import ChromeController

additional_options = ['--user-data-dir=/tmp/x']
with ChromeController.ChromeContext(binary="google-chrome", additional_options=additional_options) as cr:
    
    # Do a blocking navigate to a URL, and get the page content as served by the remote
    # server, with no modification by local javascript (if applicable)
    raw_source = cr.blocking_navigate_and_get_source("http://www.google.com")
    
    # Since the page is now rendered by the blocking navigate, we can
    # get the page source after any javascript has modified it.
    rendered_source = cr.get_rendered_page_source()
    
    # We can get the current browser URL, after any redirects.
    current_url = cr.get_current_url()
    
    # We can get the page title as the browser sees it.
    page_title, page_url = cr.get_page_url_title()
    
    # Or take a screenshot
    # The screenshot is the size of the remote browser's configured viewport,
    # which by default is set to 1024 * 1366. This size can be changed via the
    # Emulation_setVisibleSize(width, height) function if needed.
    png_bytestring = cr.take_screeshot()
    
    
    # We can spoof user-agent headers:
    new_headers = {
                'User-Agent'      : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36,gzip(gfe)', 
                'Accept-Language' : 'en-us, en;q=1.0,fr-ca, fr;q=0.5,pt-br, pt;q=0.5,es;q=0.5', 
                'Accept'          : 'image/png,  text/plain;q=0.8, text/html;q=0.9, application/xhtml+xml, application/xml, */*;q=0.1', 
                'Accept-Encoding' : 'gzip,deflate',
            }
    cr.update_headers(new_headers)
    
    
    # We can extract the cookies from the remote browser.
    # This call returns a list of python http.cookiejar.Cookie cookie
    # objects (the Chrome cookies are converted to python cookies).
    cookie_list = cr.get_cookies()
    
    # We can also set cookies in the remote browser.
    # Again, this interacts with http.cookiejar.Cookie() objects
    # directly.
    #cook = http.cookiejar.Cookie(<params>)
    #cr.set_cookie(cook)

    # We can create more tabs in the current browser context.
    # Note that these additional tabs are scoped to the same lifetime as the original 
    # chromium object (`cr`), so they will become invalid after leaving the 
    # ChromeContext() context manager.
    tab_2 = cr.new_tab()
    tab_3 = cr.new_tab()

    # At this time, multiple tabs are not thread safe, so they *probably* shouldn't 
    # be accessed concurrently. This *is* something that I'd like to change.