from googlesearch import search

def find_pdf(query):
  """
  Searches for PDFs online using Google Search.

  Args:
      query: The search terms for finding PDFs.

  Returns:
      A list of URLs containing potentially relevant PDFs.
  """
  # Add 'filetype:pdf' to search specifically for PDFs
  search_term = query + " filetype:pdf"
  results = search(search_term)  # Removed num_results argument
  return results

def main():
  """
  Prompts the user for a search query and displays results.
  """
  query = input("Enter your search query for PDFs: ")
  try:
    pdf_links = find_pdf(query)
    if pdf_links:
      print("Found PDFs:")
      for link in pdf_links:
        print(link)
    else:
      print("No PDFs found for your query.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()
