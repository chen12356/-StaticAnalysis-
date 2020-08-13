# start = time.time()
#
# async def get(url):
#     timeout = aiohttp.ClientTimeout(total=60)
#     # connector = aiohttp.TCPConnector(limit=0,verify_ssl=False)
#     async with aiohttp.ClientSession(timeout=timeout) as session:
#         async with session.get(url) as rep:
#             if rep.status == 200:
#                 return url,await rep.text()  #返回响应内容
#                 # return url, rep.headers #返回响应头信息
# async def request(url):
#     print('Waiting for', url)
#     try:
#         result = await get(url)
#
#         # print('Get response from', url, 'Result:', result)
#         return result
#     except aiohttp.ClientConnectionError as e:
#         print('{0} <-- url: {1}'.format(e,url))
#     except ValueError as e:
#         print('{0} <-- url: {1}'.format(e,url))
#     except UnicodeEncodeError as e:
#         print('{0} <-- url: {1}'.format(e,url))
#     except asyncio.futures.TimeoutError as e:
#         print('{0} <-- url: {1}'.format(e,url))
# # tasks = [asyncio.ensure_future(request(url)) for url in urls[10:20]]
# tasks = [asyncio.ensure_future(request(url)) for url in urls[0:10]]
# # print(tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# count = 0
# for task in tasks:
#     if task.result():
#         count += 1
#     # print(task.result())
# print(count)
#
# end = time.time()
# print('Cost time:', end - start)
# # =======================


# print(handle_urls_emails(datas))
# print(analytic_response(datas))
# print(test_grequsts(dat))
