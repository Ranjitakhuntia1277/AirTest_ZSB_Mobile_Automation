#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#     try:
#
#
# """---------------------------------------------------------------""""
#
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
#
# """-------------------------------------------------------------------"""
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step
#         start_time = time.time()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 2: Click on Manage Networks button. Check it would display the saved networks list
#         start_time = time.time()
# """***********************************************************"""
# def test_DataSources_TestcaseID_45729():
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Sign in the account and click My Data option'],
#         2: [2, 'Click + button at bottom and select Link File'],
#         3: [3, 'Google Drive will be opened and let user select file to link'],
#         4: [4,
#             'Select the file with Special character from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
#         5: [5,
#             'Select the file with long file name from Google Drive\nCheck the selected file is linked\nCheck the details of the File name, Source and Date added (Today) of the linked file are shown correctly'],
#         6: [6, 'Remove these 2 files\nCheck these 2 files are able to remove'],
#         7: [7, 'Repeat this test case for OneDrive'],
#         8: [8, 'Check Account Settings page should provide user management of Google and OneDrive accounts']
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#     try:
#         # Step 1: Sign in the account and click My Data option
#         start_time = time.time()
#
#         """Google Login"""
#         common_method.tearDown()
#         data_sources_page.log_out_of_account()
#         data_sources_page.clearAppData()
#         data_sources_page.allowPermissions()
#         """Sign in"""
#         registration_page.clickSignIn()
#         data_sources_page.signInWithEmail()
#         account = "zebra02.swdvt@gmail.com"
#         registration_page.sign_in_with_mail_zebra02()
#         registration_page.BugFix_For_ZebraEmail(account)
#         """verify if logged in successfully"""
#         data_sources_page.checkIfOnHomePage()
#         login_page.click_Menu_HamburgerICN()
#         """Click My Data"""
#         data_sources_page.click_My_Data()
#         sleep(2)
#         """Google Drive"""
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 2: Click + button at bottom and select Link File
#         start_time = time.time()
#
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 3: Google Drive will be opened and let user select file to link
#         start_time = time.time()
#
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         """ google drive """
#         registration_page.click_Google_Icon()
#         help_page.chooseAcc("zebra02.swdvt@gmail.com")
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         common_method.wait_for_element_appearance("NAME")
#         sleep(5)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 4: Select the file with Special character from Google Drive
#         start_time = time.time()
#
#         """Select file with special characters"""
#         special_char_file = "A_!@#$%^^&(().xlsx"
#         data_sources_page.selectFileDrive(special_char_file)
#         sleep(5)
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.verify_File_Data(special_char_file, "Google Drive")
#         data_sources_page.searchName("")
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 5: Select the file with long file name from Google Drive
#         start_time = time.time()
#
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         sleep(3)
#         """Select long file name"""
#         long_file = "1234567890qwertyuioipasdfghjklzxcvbnm0123456789qwertyuiopasdfghjklzxcvbnm123456789qwertyuiopaszxcvbn.xlsx"
#         data_sources_page.selectFileDrive(long_file)
#         sleep(5)
#         data_sources_page.searchName(long_file)
#         data_sources_page.verify_File_Data(long_file, "Google Drive")
#         data_sources_page.searchName("")
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 6: Remove these 2 files
#         start_time = time.time()
#
#         """Remove both files"""
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.remove_File_Based_On_DataSource("Google Drive", special_char_file)
#         data_sources_page.searchName("")
#         data_sources_page.searchName(long_file)
#         data_sources_page.remove_File_Based_On_DataSource("Google Drive", long_file)
#         data_sources_page.searchName("")
#         """Check if files removed successfully"""
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.checkIfListIsEmpty()
#         data_sources_page.searchName(long_file)
#         data_sources_page.checkIfListIsEmpty()
#         """"""""""""""""""""""""""""""""""""""
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 7: Repeat this test case for OneDrive
#         start_time = time.time()
#
#         """One Drive"""
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         """ One drive """
#         data_sources_page.clickMicrosoftOneDrive()
#         sleep(2)
#         data_sources_page.signInWithMicrosoft("zebra03.swdvt@gmail.com", "Zebra#123456789")
#         common_method.wait_for_element_appearance("NAME")
#         """Select file with special characters"""
#         sleep(5)
#         data_sources_page.selectFileDrive(special_char_file)
#         sleep(5)
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.verify_File_Data(special_char_file, "OneDrive")
#         data_sources_page.searchName("")
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         """ One drive """
#         data_sources_page.clickMicrosoftOneDrive()
#         data_sources_page.click_drive_sign_in_if_present()
#         sleep(3)
#         """Select long file name"""
#         data_sources_page.selectFileDrive(long_file)
#         sleep(5)
#         data_sources_page.searchName(long_file)
#         data_sources_page.verify_File_Data(long_file, "OneDrive")
#         data_sources_page.searchName("")
#         """Remove both files"""
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", special_char_file)
#         data_sources_page.searchName("")
#         data_sources_page.searchName(long_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", long_file)
#         data_sources_page.searchName("")
#         """Check if files removed successfully"""
#         data_sources_page.searchName(special_char_file)
#         data_sources_page.checkIfListIsEmpty()
#         data_sources_page.searchName(long_file)
#         data_sources_page.checkIfListIsEmpty()
#         common_method.Stop_The_App()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
#
#
# # def test_DataSources_TestcaseID_45733():
# #     """test"""
# #
# #     common_method.Start_The_App()
# #     """Click hamburger icon to expand menu"""
# #     sleep(5)
# #     login_page.click_Menu_HamburgerICN()
# #     sleep(5)
# #     """Click My Data"""
# #     data_sources_page.click_My_Data()
# #     """Click Add File"""
# #     data_sources_page.click_Add_File()
# #     """Click Upload file"""
# #     data_sources_page.click_Link_File()
# #     try:
# #         common_method.wait_for_element_appearance("NAME", 20)
# #     except:
# #         registration_page.click_Google_Icon()
# #         help_page.chooseAcc("zebra03.swdvt@gmail.com")
# #         common_method.wait_for_element_appearance("NAME")
# #     """searchTest re check"""
# #     data_sources_page.searchFilesInLinkFiles("test")
# #     sleep(4)
# #     data_sources_page.verifyFilePresentInDrive("Test1.jpg")
# #     data_sources_page.verifyFilePresentInDrive("Test2.png")
# #     data_sources_page.verifyFilePresentInDrive("Test3.bmp")
# #     data_sources_page.searchFilesInLinkFiles("test")
# #     sleep(4)
# #     data_sources_page.verifyFilePresentInDrive("Test1.jpg")
# #     """yet to write"""
# #     a = data_sources_page.getFilesShownInDrive()
# #     print(a)
# #     x=1/0
# #     """"""
# #
# #
# #     data_sources_page.searchTest("test_i", 1)
# #     data_sources_page.searchTest("test_i", 2)
# #     data_sources_page.searchTest("test_i", 3)
# #     data_sources_page.searchTest(".jpg")
# #     data_sources_page.searchTest(".png")
# #     data_sources_page.searchTest(".bmp")
# #     random_word = data_sources_page.generateRandomWord(24)
# #     data_sources_page.searchTest(random_word)
#
#
# def test_DataSources_TestcaseID_45734():
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Go to Mobile app -> My Data page'],
#         2: [2, 'Click + button at bottom and select Link File'],
#         3: [3, 'Select Google Drive'],
#         4: [4, 'Google Drive page will open and let user select file to link'],
#         5: [5, 'Select a not-supported file types to link\nCheck only supported files are listed'],
#         6: [6,
#             'Select a supported file type but file size exceed maximum allowed size (Max file size is 28.4 MB)\nCheck there is a prompt message for telling user the file is too big'],
#         7: [7,
#             'Select a same file name which already existed in app to upload\nCheck there is a prompt message for telling user the file is existed, like "file name is already linked"'],
#         8: [8, 'Repeat this test case for OneDrive, check it works same for OneDrive file']
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#     try:
#         # Step 1: Go to Mobile app -> My Data page
#         start_time = time.time()
#
#         common_method.tearDown()
#         data_sources_page.checkIfOnHomePage()
#         login_page.click_Menu_HamburgerICN()
#         sleep(2)
#         data_sources_page.click_My_Data()
#         sleep(3)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 2: Click + button at bottom and select Link File
#         start_time = time.time()
#
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 3: Select Google Drive
#         start_time = time.time()
#
#         """Test for Google Drive"""
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         data_sources_page.click_drive_sign_in_if_present()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 4: Google Drive page will open and let user select file to link
#         start_time = time.time()
#
#         common_method.wait_for_element_appearance_namematches("NAME", 20)
#         sleep(2)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 5: Select a not-supported file types to link
#         start_time = time.time()
#
#         """Cannot select unsupported file"""
#         """Modified while adding AEMS code"""
#         try:
#             data_sources_page.checkFilesShownAreSupported()
#             sleep(2)
#             x=1/0
#         except ZeroDivisionError:
#             raise Exception("There are no unsupported files shown in drive")
#         except Exception as e:
#             pass
#         """"""
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 6: Select a supported file type but file size exceed maximum allowed size
#         start_time = time.time()
#
#         """Modified while adding AEMS code"""
#         large_file = "large_unsupported_file(50mb).png"
#         try:
#             template_management_page_1.wait_for_element_appearance_name_matches_all("file too big")
#         except:
#             raise Exception("Failed due to bug SMBUI-1127")
#         """"""
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 7: Select a same file name which already existed in app to upload
#         start_time = time.time()
#
#         data_sources_page.selectFileDrive(large_file)
#         """No prompt message on uploading file greater than 28.4mb"""
#         sleep(5)
#         data_sources_page.click_Add_File()
#         sleep(2)
#         data_sources_page.click_Link_File()
#         sleep(3)
#         """Re upload same file"""
#         data_sources_page.selectFileDrive(large_file)
#         sleep(5)
#         data_sources_page.checkIsAlreadyLinkedPopUp()
#         """Remove for next execution"""
#         data_sources_page.searchName(large_file)
#         data_sources_page.remove_File_Based_On_DataSource("Google Drive", large_file)
#         data_sources_page.searchName("")
#         sleep(2)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 8: Repeat this test case for OneDrive
#         start_time = time.time()
#
#         """Test for One Drive"""
#         sleep(3)
#         data_sources_page.click_Add_File()
#         sleep(2)
#         data_sources_page.click_Link_File()
#         """ One drive """
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         sleep(2)
#         data_sources_page.clickMicrosoftOneDrive()
#         template_management_page_1.wait_for_element_appearance_name_matches_all("NAME", 20)
#         sleep(3)
#         data_sources_page.selectFileDrive(large_file)
#         sleep(5)
#         sleep(7)
#         data_sources_page.click_Add_File()
#         sleep(2)
#         data_sources_page.click_Link_File()
#         sleep(3)
#         data_sources_page.clickMicrosoftOneDrive()
#         sleep(2)
#         """Re upload the same file"""
#         data_sources_page.selectFileDrive(large_file)
#         sleep(5)
#         data_sources_page.checkIsAlreadyLinkedPopUp()
#         """Remove files for next execution"""
#         data_sources_page.searchName(large_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", large_file)
#         sleep(2)
#         common_method.Stop_The_App()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)
#
#
# def test_DataSources_TestcaseID_45735():
#     pass
#     current_function_name = inspect.currentframe().f_code.co_name
#     test_case_id = current_function_name.split("_")[-1]
#
#     test_steps = {
#         1: [1, 'Login Zebra account in Mobile app and go to My Data page'],
#         2: [2, 'Click + button at bottom and select Link File'],
#         3: [3, 'Select File page will open'],
#         4: [4, 'Select One Drive'],
#         5: [5, 'Click Back button'],
#         6: [6, 'Check mobile app return back to My Data page and no file is linked'],
#         7: [7, 'Click + button at bottom and select Link File'],
#         8: [8, 'On One Drive page, check only supported file types are listed'],
#         9: [9, 'Select a file and click Select'],
#         10: [10, 'Check mobile app return to My Data page and file is linked, Check the details of file icon, file name, Date added and Data source field (One Drive) are correct'],
#         11: [11, 'Repeat for another 2 to 3 supported file types']
#     }
#
#     start_time_main = time.time()
#     start_main(execID, leftId[test_case_id])
#
#     stepId = 1  # Initialize stepId before the try-except block
#     try:
#         # Step 1: Login Zebra account in Mobile app and go to My Data page
#         start_time = time.time()
#
#         common_method.tearDown()
#         data_sources_page.checkIfOnHomePage()
#         login_page.click_Menu_HamburgerICN()
#         sleep(2)
#         data_sources_page.click_My_Data()
#         sleep(5)
#         initial_file_count = len(data_sources_page.fileListDisplayed())
#         """One Drive"""
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 2: Click + button at bottom and select Link File
#         start_time = time.time()
#
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         """ One drive """
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 3: Select File page will open
#         start_time = time.time()
#
#         sleep(2)
#         """ One drive """
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 4: Select One Drive
#         start_time = time.time()
#
#         data_sources_page.clickMicrosoftOneDrive()
#         data_sources_page.click_drive_sign_in_if_present()
#         common_method.wait_for_element_appearance("NAME")
#         sleep(3)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 5: Click Back button
#         start_time = time.time()
#
#         data_sources_page.clickBackArrow()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 6: Check mobile app return back to My Data page and no file is linked
#         start_time = time.time()
#
#         """Check no file linked"""
#         data_sources_page.checkNoChangeInFileCount(initial_file_count)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 7: Click + button at bottom and select Link File
#         start_time = time.time()
#
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 8: On One Drive page, check only supported file types are listed
#         start_time = time.time()
#
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         """ One drive """
#         data_sources_page.clickMicrosoftOneDrive()
#         template_management_page_1.wait_for_element_appearance_name_matches_all("NAME", 20)
#         sleep(5)
#         data_sources_page.checkFilesShownAreSupported()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 9: Select a file and click Select
#         start_time = time.time()
#
#         png_file = "png_file.png"
#         data_sources_page.selectFileDrive(png_file)
#         sleep(5)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 10: Check mobile app return to My Data page and file is linked, Check the details of file icon, file name, Date added and Data source field (One Drive) are correct
#         start_time = time.time()
#
#         data_sources_page.searchName(png_file)
#         data_sources_page.verifyFilePresentInList(png_file, "OneDrive", True)
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#         stepId += 1
#
#         # Step 11: Repeat for another 2 to 3 supported file types
#         start_time = time.time()
#
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         """ One drive """
#         data_sources_page.clickMicrosoftOneDrive()
#         common_method.wait_for_element_appearance("NAME")
#         sleep(5)
#         jpg_file = "jpg_file.jpg"
#         data_sources_page.selectFileDrive(jpg_file)
#         sleep(5)
#         data_sources_page.searchName(jpg_file)
#         data_sources_page.verifyFilePresentInList(jpg_file, "OneDrive", True)
#         """Click Add file"""
#         data_sources_page.click_Add_File()
#         sleep(2)
#         """Click Link File"""
#         data_sources_page.click_Link_File()
#         template_management_page_1.wait_for_element_appearance_name_matches_all("Microsoft OneDrive", 20)
#         """ One drive """
#         data_sources_page.clickMicrosoftOneDrive()
#         common_method.wait_for_element_appearance("NAME")
#         sleep(5)
#         bmp_file = "bmp_file.bmp"
#         data_sources_page.selectFileDrive(bmp_file)
#         sleep(5)
#         data_sources_page.searchName(bmp_file)
#         data_sources_page.verifyFilePresentInList(bmp_file, "OneDrive", True)
#         """Remove files for next execution"""
#         data_sources_page.searchName("")
#         data_sources_page.searchName(png_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", png_file)
#         data_sources_page.searchName("")
#         data_sources_page.searchName(jpg_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", jpg_file)
#         data_sources_page.searchName("")
#         data_sources_page.searchName(bmp_file)
#         data_sources_page.remove_File_Based_On_DataSource("OneDrive", bmp_file)
#         data_sources_page.searchName("")
#         common_method.Stop_The_App()
#
#         exec_time = (time.time() - start_time) / 60
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Pass",
#                     exec_time)
#
#     except Exception as e:
#         screenshot_path, _ = common_method.capture_screenshot(stepId, test_case_id)
#         insert_step(execID, leftId[test_case_id], test_steps[stepId][0], stepId, test_steps[stepId][1], "Fail", 0)
#         insert_stepDetails(execID, leftId[test_case_id], test_steps[stepId][0], str(e), "")
#         insert_case_results(execID, leftId[test_case_id], "Fail", 0, str(e), str(e))
#         upload_case_files(execID, os.path.dirname(screenshot_path), test_run_start_time)
#         raise Exception(str(e))
#
#     finally:
#         end_main(execID, leftId[test_case_id], (time.time() - start_time_main) / 60)