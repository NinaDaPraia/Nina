require 'spec_helper'
require 'pacto/rspec'
require 'pacto/test_helper'

describe 'API consumer' do
  include Pacto::TestHelper

  let(:endpoint) { "#{API_HOST}/influential_figures" }

  it 'gets the influential figures' do
    with_pacto(
      :port => 8000,
      :live => true,
      :stub => false
    ) do |pacto_endpoint|
      Net::HTTP.get(URI(endpoint))
      expect(Pacto).to have_validated(:get, endpoint)
    end
  end
end