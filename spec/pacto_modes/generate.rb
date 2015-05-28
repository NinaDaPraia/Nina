Pacto::Generator.configure do |c|
  c.hint 'API root endpoint', http_method: :get, host: API_HOST, path: '/'
  c.hint 'GET influential figures', http_method: :get, host: API_HOST, path: '/influential_figures'
end

Pacto.generate!