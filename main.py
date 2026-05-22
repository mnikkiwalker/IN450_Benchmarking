import generate_list as gd
import bubble_sort
import quick_sort as qs


#generating lists for sorting
small_list = gd.generate_list(100)
medium_list = gd.generate_list(1000)
large_list = gd.generate_list(10000)

#original list
# print()
# print("Original List")
# print("-"*20)
# for i, number in enumerate(small_list):
#     print(i+1," - ",number)


##################sort list - bubble sort
print()
print("Original Algorithm Summary")
print("-"*20)

#small list
small_list_sorted, small_list_duration = bubble_sort.loop_bubble_sort(small_list)
s_duration_ms = format(small_list_duration * 1000, ".0f")
print("Small Sorted List duration: ", s_duration_ms, "ms")

#medium list
medium_list_sorted, medium_list_duration = bubble_sort.loop_bubble_sort(medium_list)
m_duration_ms = format(medium_list_duration * 1000, ".0f")
print("Medium Sorted List duration: ", m_duration_ms, "ms")

#large list
large_list_sorted, large_list_duration = bubble_sort.loop_bubble_sort(large_list)
l_duration_ms = format(large_list_duration * 1000, ".0f")
print("Large Sorted List duration: ", l_duration_ms, "ms")



##################sort list - modified
print()
print("Modified Algorithm Summary")
print("-"*20)

#small list
small_list_sorted, small_list_duration = qs.quicksort_run(small_list)
s_duration_ms = format(small_list_duration * 1000, ".0f")
print("Small Sorted List duration: ", s_duration_ms, "ms")

#medium list
medium_list_sorted, medium_list_duration = qs.quicksort_run(medium_list)
m_duration_ms = format(medium_list_duration * 1000, ".0f")
print("Medium Sorted List duration: ", m_duration_ms, "ms")

#large list
large_list_sorted, large_list_duration = qs.quicksort_run(large_list)
l_duration_ms = format(large_list_duration * 1000, ".0f")
print("Large Sorted List duration: ", l_duration_ms, "ms")

print()